import unittest2


from StringIO import StringIO
from hanzo.httptools.messaging import RequestMessage, ResponseMessage


get_request = "\r\n".join( [
    "GET / HTTP/1.1",
    "Host: example.org",
    "",
    "",
])
get_response = "\r\n".join( [
    "HTTP/1.1 200 OK",
    "Host: example.org",
    "Content-Length: 5",
    "",
    "tests",
])


class GetTest(unittest2.TestCase):

    def runTest(self):
        print repr(get_request)
        p = RequestMessage()
        for t in get_request:
            print t
            text = p.feed(t)
            print t, text
            self.assertEqual(text, '')
        self.assertTrue(p.complete())


        self.assertEqual(get_request, p.get_decoded_message())
        print repr(get_response)
        
        p = ResponseMessage(p)
        text = p.feed(get_response)

        self.assertEqual(text, '')
        self.assertTrue(p.complete())
        self.assertEqual(get_response, p.get_decoded_message())

head_request = "\r\n".join( [
    "HEAD / HTTP/1.1",
    "Host: example.org",
    "",
    "",
])
head_response = "\r\n".join( [
    "HTTP/1.1 200 OK",
    "Host: example.org",
    "Content-Length: 5",
    "",
    "",
])


class HeadTest(unittest2.TestCase):

    def runTest(self):
        print repr(head_request)
        p = RequestMessage()
        text=p.feed(head_request)

        self.assertEqual(text, '')
        print p.mode
        print p.feed_predict()
        self.assertTrue(p.complete())
        self.assertEqual(head_request, p.get_decoded_message())

        print repr(head_response)

        
        p = ResponseMessage(p)
        text = p.feed(head_response)

        self.assertEqual(text, '')
        self.assertTrue(p.complete())
        self.assertEqual(head_response, p.get_decoded_message())

post_request = "\r\n".join( [
    "POST / HTTP/1.1",
    "Host: example.org",
    "Transfer-Encoding: chunked",
    "",
    "8",
    "abcdefgh",
    "0",
    "",
    "",
])
post_response = "\r\n".join( [
    "HTTP/1.1 100 Continue",
    "Host: example.org",
    "",
    "HTTP/1.0 204 No Content",
    "Date: now!",
    "",
    "",
])


class PostTest(unittest2.TestCase):

    def runTest(self):
        print repr(post_request)
        p = RequestMessage()
        text = p.feed(post_request)

        self.assertEqual(text, '')
        self.assertTrue(p.complete())

        print repr(post_response)

        
        p = ResponseMessage(p)
        text = p.feed(post_response)
        

        self.assertEqual(text, '')
        self.assertTrue(p.complete())


if __name__ == '__main__':
    unittest2.main()


