#!/usr/bin/env python3
"""Simple API test script"""
import json
import urllib.request
import urllib.error

def test_api(description):
    """Test the API endpoint"""
    url = 'http://localhost:5000/api/process-car'
    data = json.dumps({'description': description}).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())
            print(f"Status: {response.status}")
            print(f"Response: {json.dumps(result, indent=2)}")
    except urllib.error.HTTPError as e:
        result = json.loads(e.read())
        print(f"Status: {e.code}")
        print(f"Response: {json.dumps(result, indent=2)}")

if __name__ == '__main__':
    print("=" * 60)
    print("TEST 1: Empty description")
    print("=" * 60)
    test_api('')
    
    print("\n" + "=" * 60)
    print("TEST 2: Short description (less than 20 chars)")
    print("=" * 60)
    test_api('test short')
