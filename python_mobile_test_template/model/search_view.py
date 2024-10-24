from selene.support._mobile import device


class Search:
    input = device.element('search_src_text')
    resultTitles = device.all('page_list_item_title')
