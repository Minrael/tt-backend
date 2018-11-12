#! /usr/bin/env python3

import sys
import base64

if __name__ =="__main__":
  if len( sys.argv ) != 2:
    print( "Usage: {} filename".format( sys.argv[0] ) )
    sys.exit(1)
  filename = sys.argv[1]

  with open( filename, 'rb' ) as input_file:
    content = input_file.read()
    b64_content = base64.b64encode( content ).decode('utf8')
    print( b64content )

    response = service.api.upload_file( b64 -content, filename )
    print( "Response: {}".format( response ) )
