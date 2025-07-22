from scraping.config import SELECTORS
from scraping.safeGet import safe_get


async def extract_data_from_page(page):
    data = []
    base_url = "https://www.centris.ca"

    cards = page.locator(SELECTORS["cards"]["container"])
    count = await cards.count()

    for i in range(count):
        card = cards.nth(i)

        titre = await safe_get(card.locator(SELECTORS["cards"]["title"]), "content")
        mls = await safe_get(card.locator(SELECTORS["cards"]["mls"]), "content")
        lien = await safe_get(card.locator(SELECTORS["cards"]["link"]), "href")
        image = await safe_get(card.locator(SELECTORS["cards"]["image"]), "src")
        prix = await safe_get(card.locator(SELECTORS["cards"]["price"]))
        type_ = await safe_get(card.locator(SELECTORS["cards"]["type"]))
        rue = await safe_get(card.locator(SELECTORS["cards"]["street"]))
        ville = await safe_get(card.locator(SELECTORS["cards"]["city"]))
        superficie = await safe_get(card.locator(SELECTORS["cards"]["area"]))

        data.append({
            "Titre": titre,
            "MLS": mls,
            "Lien": base_url + lien if lien != "-" else "-",
            "Image": image,
            "Prix": prix,
            "Type": type_,
            "Rue": rue,
            "Ville": ville,
            "Superficie": superficie
        })

    return data
