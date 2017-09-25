## Summary
Trading bot which executed trades on a simulated marketplace run on the `Amazon EC2` during the `Jane Street` electronic trading competition. Calculated fair price values for a range of tradeable commodities on the simulated market generated by `Jane Street`. `Grew` an initial amount of `$30,000 to $73,200` at the end of a `12 hour` trading session.

## About The Competition
The `Electronic Trading Challenge` is a `12-hour` marathon where teams write a bot that can `parse` a `custom exchange protocol`, and a strategy to compete with others. The goal is to write a program that will make money by `trading securities` on a financial exchange. Other participants in the market will be other people's programs, and also some programs provided by us (the "marketplace bots"). We will be running this competition on `Amazon EC2`.

Each team will receive one `Ubuntu Linux box` in the `cloud` which is yours and yours alone, which we'll call your "bot box". You can develop there if you wish, or you can develop on your laptop and upload to your box. If you choose the latter route, be sure to check that your `binary` actually works in the `cloud`.

![Jane Street Logo](https://i.imgur.com/Thqrmo5.jpg?raw=true) ![Image of ETC Logo](https://i.imgur.com/wcc6BgL.png?raw=true)


## Connecting To The Marketplace
We were given `three ports` to connect to test our bot. There were three exchanges the `first` one being the `zeroth exchange`, which ran at `competition speed` and was optimal for testing how `efficiently` our bot would run on the competition's marketplace `in real time`. The `first exchange` was designed to operate `more slowly`, and the `second exchange` was `empty` of any outside trades, only inputted one's by the team using it to `debug` the `behavior` of their bot. Our bot needed to establish a `TCP connection` the exchange, and had to establish said connection with any of the the proper port that supported the `JSON protocol`, since that was how we chose to `parse activity on the marketplace`, rather than using a `plain-text protocol`. When the bot was `pushed` to the `production port`, the bot ran on the `competition marketplace`, generating `profits` and `conducting trades` in the `same marketplace` as all other `competitor bots` on an instance of the `Amazon EC2`. Below is a schematic of the `distributed system`.

![Amazon Web Services Logo](https://i.imgur.com/LXZKCvZ.png?raw=true)

![EC2 Schematic](https://i.imgur.com/tagMefL.png?raw=true)


## Trading Algorithm
The general `algorithm` of the bot we designed was to calculate a `running average` of the `spread` of all the different `commodities` on the marketplace from the start to the end of the competition to determine the `'fair price'` to `trade` the `commoditiy` for. 

**_> Any commodity bought under the running 'fair price' is considered a good buy with respect to profit after a very long time._**

**_> Any commodity sold over the running 'fair price' is considered a good sell with respect to profit after a very long time._**

While the `running average` may have been `volatile` at the beginning of the competition due to `inconsistencies in the market`, after an hour of trading the values of the commodities may have gone up and down by several dollars, whereas the `'fair price'` value for that `commodity` ultimately **stayed the same.** Across `12 hours`, this algorithm earned a `profit` of `$43,200`.



