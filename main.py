from flask import Flask, Response, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/v1/endpoint")
def generate_xml():
    result = ET.Element('result')

    has_error = ET.SubElement(result, 'has_error')
    has_error.text = '0'

    version = ET.SubElement(result, 'version')
    version.text = '1'

    endpoint = ET.SubElement(result, 'endpoint')

    host = ET.SubElement(endpoint, 'host')
    host.text = request.host

    api_host = ET.SubElement(endpoint, 'api_host')
    api_host.text = 'API_HOST'

    portal_host = ET.SubElement(endpoint, 'portal_host')
    portal_host.text = 'PORTAL_HOST'

    n3ds_host = ET.SubElement(endpoint, 'n3ds_host')
    n3ds_host.text = '3DS_HOST'

    xml_declaration = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    xml_string = xml_declaration + ET.tostring(result, encoding='unicode')

    response = Response(xml_string, content_type='application/xml')
    response.headers['Content-Length'] = str(len(xml_string.encode('utf-8')))
    return response

if __name__ == "__main__":
    app.run(port=5000)
