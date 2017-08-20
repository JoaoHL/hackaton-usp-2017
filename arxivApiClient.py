import urllib
import sys
import xml.dom.minidom
from xml.dom.minidom import parse
import json
from json import JSONEncoder as encoder


def getPaperList(terms, n):
	query = ""
	for term in terms:
		query += "+OR+abs:\"" + term + "\""
	query = query[9:]
	url = "http://export.arxiv.org/api/query?search_query=abs:\"" + query + "&sortBy=lastUpdatedDate&sortOrder=ascending&max_results=" + str(n)
	data = urllib.urlopen(url).read()
	return data

if (len(sys.argv) > 1):
	terms = []
	for i in range(len(sys.argv)):
		if (i > 0):
			terms.append(sys.argv[i])
	x = getPaperList(terms, 3)
	tree = xml.dom.minidom.parseString(x)
	doc = tree.documentElement
	entries = doc.getElementsByTagName("entry")
	jsonEntries = []
	for entry in entries:
		properties = ["title", "published", "summary"]
		x = [(y, entry.getElementsByTagName(y)[0].firstChild.nodeValue) for y in properties]
		author = entry.getElementsByTagName("author")[0]
		author = author.getElementsByTagName("name")[0].firstChild.nodeValue
		x.append(("author", author))
		score = 0
		abstract = entry.getElementsByTagName("summary")[0].firstChild.nodeValue 
		for term in terms:
			if (term in abstract): score += 1
		x.append(("score", str(int(100 * score / float(len(terms))))))
		jsonEntries.append(x)

	outputJson = []
	for entry in jsonEntries:
		jsonEntry = {}
		jsonEntry["entry"] = {}
		for field in entry:
			jsonEntry["entry"][field[0]] = field[1]
		categories = []
		for term in terms:
			if (term in jsonEntry["entry"]["summary"]):
				categories.append(term)
		jsonEntry["entry"]["categories"] = categories
		outputJson.append(jsonEntry)

	outputJson = encoder().encode(outputJson)
	print(outputJson)





