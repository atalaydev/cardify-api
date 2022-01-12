from buckets.router import router as BucketsRouter
from cards.router import router as CardsRouter

router_urls = BucketsRouter.urls + CardsRouter.urls
