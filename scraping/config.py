URL = 'https://www.centris.ca/fr/propriete~a-vendre~quebec-peripherie-nord'

PAGE_TIME_OUT = 60000

SELECTORS = {
    "popUp": "h2.didomi-popup-notice-h2-custom",
    "closePopUp": "button[id='didomi-notice-agree-button']",
    "nextButton": "#divPagerBottom li.next:not(.disabled)",
    "zone": "li[data-searchfilterid='GeographicSubArea']",
    "resultCount": "span.js-resultCount",
    "resultContainer": "#divMainResult",
    "cards": {
        "container": "div.shell",
        "title": 'meta[itemprop="name"]',
        "mls": 'meta[itemprop="sku"]',
        "link": 'a.property-thumbnail-summary-link',
        "image": 'a.property-thumbnail-summary-link img',
        "price": 'div.price-section span:first-of-type',
        "type": 'div.category > div',
        "street": 'div.address > div:nth-child(1)',
        "city": 'div.address > div:nth-child(2)',
        "area": 'div.land-area > span'
    }
}