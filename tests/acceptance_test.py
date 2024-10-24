from selene import have

from python_mobile_test_template.model import app


def test_wikipedia_searches():
    # GIVEN
    app.onboarding.Skip.tap()

    # WHEN
    app.feed.search_icon.tap()
    app.search.input.type('Appium')

    # THEN
    app.search.resultTitles.should(have.size_greater_than(0))
    app.search.resultTitles.first.should(have.text('Appium'))

    # WHEN
    app.search.resultTitles.first.tap()

    # THEN
    app.page.should_have_element_with_text('Appium')
