import texttranslation
import doctranslation
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-p", "--projectid", help="gcp project id")
argParser.add_argument("-i", "--translatetext", help="The text that you like to translate")
argParser.add_argument("-s", "--sourcelang", help="the source language")
argParser.add_argument("-t", "--targetlang", help="the target language")

args = argParser.parse_args()
print("args=%s" % args)

print("args.projectid=%s" % args.projectid)
print("args.translatetext=%s" % args.translatetext)
print("args.sourcelang=%s" % args.sourcelang)
print("args.targetlang=%s" % args.targetlang)

# texttranslation.translate_text(args.translatetext, args.projectid, args.sourcelang, args.targetlang)
doctranslation.translate_document(args.projectid, args.sourcelang, args.targetlang)