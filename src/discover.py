import os

def discover_files(directory):
  """
  Discovers all files in a directory and its subdirectories.
  Args:
    directory: The directory to search.
  Returns:
    A list of all files in the directory and its subdirectories.
  """
  files = []
  for root, dirs, files_in_dir in os.walk(directory):
    for file in files_in_dir:
      files.append(os.path.join(root, file))
  return files


def extract_text_from_docx(docx_file):
  """Extracts text from a docx file.
  Args:
    docx_file: The path to the docx file.
  Returns:
    The text content of the docx file.
  """
  from docx import Document
  document = Document(docx_file)
  text = ""
  for paragraph in document.paragraphs:
    text += paragraph.text + "\n"
  return text


def discover(Secure1PSID, directory = ".\SmartEDiscovery-main\EIS"):
  from Bard import Chatbot
  chatbot = Chatbot(Secure1PSID)
  files = discover_files(directory)
  for file in files:
    corpse = '''#following are the contents of "{}" document \n#Return only "YES Done READING"  sentence if you read once you read all the lines\n\n'''.format(file)
    print("[Reading] : {}".format(file))
    if ".docx" in file:
      corpse += extract_text_from_docx(file)
    else:
      with open(file, "r") as f:
        corpse += str(f.readlines())
    res=chatbot.ask(corpse)
    #print(res)
    if "YES Done READING" in res["content"]:
      print("Reading Success")
    else:
      print("Reading Failed")
    #print(res["content"])

  while(1):
    n=input("\nQuestion : ")
    if(n=='!exit'):
      break
    else:
      print("Bard : ")
      print(chatbot.ask(n)["content"])


if __name__ == "__main__":
  Secure1PSID=input("Enter the Secure1PSID : ")
  directory = input("Enter the Directory : ")
  discover(Secure1PSID)
