from scraping.config import BASE_URL, SELECTORS
from scraping.safeGet import safe_get

async def extract_data_from_page(page):
    data = []
   
    cards = page.locator(SELECTORS["cards"]["container"])
    count = await cards.count()

    for i in range(count):
        card = cards.nth(i)

        titre = await safe_get(card.locator(SELECTORS["cards"]["title"]), "content")
        lien = await safe_get(card.locator(SELECTORS["cards"]["link"]), "href")
        image = await safe_get(card.locator(SELECTORS["cards"]["image"]), "src")
        prix = await safe_get(card.locator(SELECTORS["cards"]["price"]))
        type_ = await safe_get(card.locator(SELECTORS["cards"]["type"]))
        rue = await safe_get(card.locator(SELECTORS["cards"]["street"]))
        ville = await safe_get(card.locator(SELECTORS["cards"]["city"]))
        superficie = await safe_get(card.locator(SELECTORS["cards"]["area"]))

        data.append({
            "Titre": titre,
            "Lien":  BASE_URL + lien if lien != "-" else "-",
            "Image": image,
            "Prix": prix,
            "Type": type_,
            "Rue": rue,
            "Ville": ville,
            "Superficie": superficie
        })

    return data
