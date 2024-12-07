import pymupdf, sys, pathlib

def main():
  filename = pathlib.Path(sys.argv[1])
  print(filename)
  with pymupdf.open(filename) as document:
    text = chr(12).join([page.get_text() for page in document])
  print(text)


if __name__ == '__main__':
  main()
