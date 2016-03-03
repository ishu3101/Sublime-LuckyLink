import sublime
import sublime_plugin
import urllib
import urllib2
import json

class LuckyLinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            selected_text = self.view.substr(region)
            url = self.getLuckyLink(selected_text)
            result = url
            self.view.replace(edit, region, result)

    def getLuckyLink(self, inputphrase):
        terms = urllib.quote_plus(inputphrase.strip())
        url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&filter=1&rsz=small&q=" + terms
        data = urllib2.urlopen(url).read()
        link = json.loads(data)["responseData"]["results"][0]["unescapedUrl"];
        output =  link
        return output