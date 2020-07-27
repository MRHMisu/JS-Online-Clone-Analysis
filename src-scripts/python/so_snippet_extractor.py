"""
Extract code snippets from the SO dump (Posts.xml) file for all accepted answer based on a language tag.
And create a xml file containing all extracted snippets including LOC.
"""

# Example snippets of Posts.xml
# <row Id="4" PostTypeId="1" AcceptedAnswerId="7" Tags="&lt;discussion&gt;" AnswerCount="2" CommentCount="0" />
# <row Id="7" PostTypeId="2" ParentId="4" />
# PostTypeId="1" represents Question and PostTypeId="2" represents Answer


import sys;
from xml.etree import ElementTree as ET


def extract_code_snippets(posts_xml_path, language_tag, code_snippet_output, batch_size):
    xml_parser = ET.iterparse(posts_xml_path)
    accepted_answers_ids = set()
    accepted_answers_code_snippets = set()
    code_snippets_count = 0
    for rc, (event, element) in enumerate(xml_parser):
        if element.tag == "row":
            if element.get("PostTypeId") == "1":  # explore the question
                if element.get("AcceptedAnswerId") and language_tag in element.get("Tags"):
                    accepted_answers_ids.add(element.get("AcceptedAnswerId"))
            elif element.get("PostTypeId") == "2":  # explore the answer
                answer_id = element.get("Id")
                question_id = element.get("ParentId")
                if answer_id in accepted_answers_ids:
                    accepted_answers_ids.remove(answer_id)
                    populate__code_snippets_as_csv(element, accepted_answers_code_snippets, question_id, answer_id)
                    code_snippets_count += store_code_snippets_in_batch(accepted_answers_code_snippets,
                                                                        code_snippet_output, batch_size,
                                                                        code_snippets_count)

        element.clear()
    write_lines(accepted_answers_code_snippets, code_snippet_output)


def populate__code_snippets_as_csv(element, accepted_answers_code_snippets, question_id, answer_id):
    accepted_answer = "<?xml version=\"1.0\"?>" + '\n' + "<answer>" + element.get("Body") + "</answer>" + '\n'
    try:
        root = ET.fromstring(accepted_answer)
        block_position = 0
        for snippet in root.iter('code'):  # explore all <code>*</code> elements
            block_position += 1
            code = snippet.text
            if code and not code.isspace():
                line_of_code = len(code.splitlines())
                # if line_of_code > 0:  # only takes sinippets that contains at least n lines
                complete_element = question_id + "," + answer_id + "," + str(block_position) + "," + str(
                    line_of_code) + "," + code.encode().hex() + '\n'
                accepted_answers_code_snippets.add(complete_element)
    except ET.ParseError:
        return


def store_code_snippets_in_batch(accepted_answers_code_snippets, code_snippet_output, batch_size, code_snippets_count):
    if len(accepted_answers_code_snippets) >= batch_size:
        write_lines(accepted_answers_code_snippets, code_snippet_output)
        accepted_answers_code_snippets.clear()
        print("Collecting " + str(code_snippets_count) + " code snippets...")
        return batch_size
    else:
        return 0


def write_lines(contents, path):
    file_writer = open(path, 'a')
    file_writer.writelines(contents)
    file_writer.close()


if __name__ == "__main__":
    # stackoverflow.com-Posts.7z (View Contents)	02-Jun-2020 01:04	15.1G
    # run with 4 command line arguments
    # python code_snippet_extractor.py sample-posts.xml language output.csv batch_size
    so_post_xml_path = sys.argv[1]
    language_tag = sys.argv[2]
    code_snippet_output = sys.argv[3]
    batch_size = int(sys.argv[4])

    header = "question_id" + "," + "answer_id" + "," + "block_position" + "," + "loc" + "," + "code_snippet" + '\n'
    write_lines(header, code_snippet_output)
    extract_code_snippets(so_post_xml_path, language_tag, code_snippet_output, batch_size)
    sys.exit()
