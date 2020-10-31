import shodan

y = raw_input("Enter your server:")
x = raw_input("Enter your key:")
SHODAN_API_KEY = (x)

api = shodan.Shodan(SHODAN_API_KEY)

try:
            #Search Shodan
            results = api.search(y)

            # Show the results

            for result in results['matches']:
                    print '%s' % result['ip_str']

except shodan.APIError, e:
        print 'Error: %s' % e


