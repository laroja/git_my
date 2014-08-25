import sys
import argparse
import os
import gdata.data
import gdata.docs.client
import gdata.docs.data
import gdata.docs.service
import gdata.sample_util

class SampleConfig(object):
  APP_NAME = 'GDataDocumentsListAPISample-v1.0'
  DEBUG = False

def create_client():
  client = gdata.docs.client.DocsClient(source=SampleConfig.APP_NAME)
  try:
    gdata.sample_util.authorize_client(
       client,
       1,
       service=client.auth_service,
       source=client.source,
       scopes=client.auth_scopes
    )
  except gdata.client.BadAuthentication:
    exit('Invalid user credentials given.')
  except gdata.client.Error:
    exit('Login Error')
  return client

def upload_file(path, title, type, do_convert):
  client = create_client()
  doc = gdata.docs.data.Resource(type=type, title=title)
  media = gdata.data.MediaSource()
  media.SetFileHandle(path, type)
  create_uri = gdata.docs.client.RESOURCE_UPLOAD_URI + '?convert=' + do_convert
  doc = client.CreateResource(doc, create_uri=create_uri, media=media)
  print 'Uploaded:', doc.title.text, doc.resource_id.text

def main():
  parser = argparse.ArgumentParser(description='Upload file to Google Drive (previously known as \'Google Docs\').')
  parser.add_argument('file', help='file to upload.')
  parser.add_argument('title', help='title for the uploaded document.')
  parser.add_argument('type', nargs='?', default='text/plain', help='type of file to upload, default is text/plain.')
  parser.add_argument('do_convert', nargs='?', default='true', help='true or false: convert the document to Google Docs format? Default is true')
  args = parser.parse_args()
  path = args.file
  title = args.title
  type = args.type
  do_convert = args.do_convert
  upload_file(path, title, type, do_convert)
  os._exit(0)

# Specifies name of main function.
if __name__ == "__main__":
  sys.exit(main())
