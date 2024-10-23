import scrapy


class DogwoodCenterSpider(scrapy.Spider):
    name = "dogwood_center"
    allowed_domains = ["dogwoodcenter.com"]
    start_urls = ["https://dogwoodcenter.com/events"]

    def parse(self, response):
        for element in response.css('header.tribe-events-calendar-list__event-header'):
            title = element.css('h3 a::text').get().strip()
            link = element.css('h3 a::attr(href)').get()
            datetime_info = element.css('time.tribe-events-calendar-list__event-datetime').attrib.get('datetime')
            venue_name = element.css('address .tribe-events-calendar-list__event-venue-title::text').get().strip()
            venue_address = element.css('address .tribe-events-calendar-list__event-venue-address::text').get().strip()

            item = {
                'title': title,
                'link': link,
                'datetime': datetime_info,
                'venue': {
                    'name': venue_name,
                    'address': venue_address
                }
            }

            yield item