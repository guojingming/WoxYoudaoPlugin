# -*- coding: utf-8 -*-

from wox import Wox
import translation

class HelloWorld(Wox):
    def query(self, query):
        results = []
        arrayResult = translation.getTranslationResult(query)
        for res in arrayResult:
            results.append({
                "Title": "Hello World",
                "SubTitle": res,            
                "IcoPath":"Images/app.ico"
            })
        return results

if __name__ == "__main__":
    HelloWorld()