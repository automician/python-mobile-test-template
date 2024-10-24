from selene.support._mobile import device


class Feed:
    search_icon = device.element(drd='Search Wikipedia')
    SearchWikipedia = device.element('text="Search Wikipedia"')
