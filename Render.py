"""Output Parsed Links In Html Format"""

result = ["afasdf", "wqetqwer", "esdfgasdg", "eafasgsdfg"]

def RenderToHTML(result):
    html = "<html>\n\t<body>\n\t\t<h1> URL results </h1>\n\t\t<ul>"
    html += "\n\t\t\t".join("<a>" + str(item) + "</a>" for item in result)
    html += "\n\t\t</ul>\n\t</body>\n</html>"

    raise Exception("Rendering to HTML is not completed!")

    return html

"""Raw Code for Rendering HTML"""
# html = '''
# <html>
#     <body>
#         <h1>URL results</h1>
#         <div>
#             <a>''' + extracted_cards[18].attrs['href'] + '''</a>
#         </div>
#     </body>
# </html>
# '''
# html_output = open("output.html", "w")
# html_output.write(html)
# html_output.close()

# Notes: extracted_cards[18].attrs['href']  