import pymupdf, sys, pathlib, os, glob
from fuzzywuzzy import fuzz

def main():
  searchDir = pathlib.Path(sys.argv[1])
  print(searchDir)
  directory = os.path.abspath(searchDir)
  pdf_files = glob.glob(os.path.join(directory, "**", "*.pdf"), recursive=True)
  # files = []
  # for path, _, files in os.walk(searchDir):
  #   print(files)
  #   for name in files:
  #     print(name)
  #     if name.endswith('.pdf'):
  #       files.append(pathlib.PurePath(path, name))
  #   print("--")
        
  print(pdf_files)
  lookup = {}
  for f in pdf_files:
    lookup[f] = []
    with pymupdf.open(f) as document:
      for page in document:
        lookup[f].append(page.get_text())

  while True:
    search = input("Search Phrase: ")
    for file in lookup.keys():
      for pagenum, page  in enumerate(lookup[file]):
        m = fuzz.partial_ratio(page.lower(), search.lower())
        if m > 70:
          print(f'{file} : {pagenum} : {m}')  
if __name__ == '__main__':
  main()
