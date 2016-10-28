from app.models import Transaction, PortfolioAssetMapping, Asset
from yahoo_finance import Share
from datetime import datetime


class TransactionApi():
    def addTransaction(self, trade, tradeCount, assetSymbol):
        asset = Asset.objects.get(symbol=assetSymbol)
        portfolioAssetMapping = PortfolioAssetMapping.objects.get(asset=asset)
        timestamp = "2012-01-03"

        initialCount = portfolioAssetMapping.currentCount
        finalCount = initialCount
        if trade == "buy":
            finalCount = initialCount + tradeCount
        if trade == "sell":
            finalCount = initialCount - tradeCount

        portfolioAssetMapping.currentCount = finalCount

        assetInfo = Share(assetSymbol)
        price = finalCount * float(assetInfo.get_price())
        transaction = Transaction(mapping=portfolioAssetMapping, trade=trade, timestamp=timestamp,
                                  initialCount=initialCount,
                                  finalCount=finalCount, tradeCount=tradeCount, price=price)
        transaction.save()
        portfolioAssetMapping.save()
