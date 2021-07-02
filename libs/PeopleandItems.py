import requests
import json

class PeopleandItems:

    def __init__(self, customerId):
        self.customerId = customerId

    def getId(self):
        return self.customerId

    def addInvoice(self, invoice):
        self.invoice = invoice

    def getInvoice(self):
        return self.invoice

    def addInvoicer(self, invoicer):
        self.invoicer = invoicer

    def createInvoiceDraft(self, date, currency_code, note, term, memo, term_type, due_date):
        authorization = "Bearer " + self.access_token
        headers = {
            'Content-Type': 'application/json',
            'Authorization': authorization,
        }

        response = requests.post('https://api-m.sandbox.paypal.com/v2/invoicing/generate-next-invoice-number',
                                 headers=headers)
        respjson = response.json()
        print(respjson)
        invoice_number = respjson['invoice_number']
        print(invoice_number)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': authorization,
        }

        data = {
            "detail": {
                "invoice_number": invoice_number,
                "reference": "deal-ref",
                "invoice_date": "2018-11-12",
                "currency_code": "USD",
                "note": "Thank you for your business.",
                "term": "No refunds after 30 days.",
                "memo": "This is a long contract",
                "payment_term": {
                    "term_type": "NET_10",
                    "due_date": "2018-11-22"
                }
            },
            "invoicer": {
                "name": {
                    "given_name": "David",
                    "surname": "Larusso"
                },
                "address": {
                    "address_line_1": "1234 First Street",
                    "address_line_2": "337673 Hillside Court",
                    "admin_area_2": "Anytown",
                    "admin_area_1": "CA",
                    "postal_code": "98765",
                    "country_code": "US"
                },
                "email_address": "sudhan.annamalai@rocketbot.com",
                "phones": [
                    {
                        "country_code": "001",
                        "national_number": "4085551234",
                        "phone_type": "MOBILE"
                    }
                ],
                "website": "www.test.com",
                "tax_id": "ABcNkWSfb5ICTt73nD3QON1fnnpgNKBy- Jb5SeuGj185MNNw6g",
                "logo_url": "https://example.com/logo.PNG",
                "additional_notes": "2-4"
            },
            "primary_recipients": [
                {
                    "billing_info": {
                        "name": {
                            "given_name": "Stephanie",
                            "surname": "Meyers"
                        },
                        "address": {
                            "address_line_1": "1234 Main Street",
                            "admin_area_2": "Anytown",
                            "admin_area_1": "CA",
                            "postal_code": "98765",
                            "country_code": "US"
                        },
                        "email_address": "sudhan102002@gmail.com",
                        "phones": [
                            {
                                "country_code": "001",
                                "national_number": "4884551234",
                                "phone_type": "HOME"
                            }
                        ],
                        "additional_info_value": "add-info"
                    },
                    "shipping_info": {
                        "name": {
                            "given_name": "Stephanie",
                            "surname": "Meyers"
                        },
                        "address": {
                            "address_line_1": "1234 Main Street",
                            "admin_area_2": "Anytown",
                            "admin_area_1": "CA",
                            "postal_code": "98765",
                            "country_code": "US"
                        }
                    }
                }
            ],
            "items": [
                {
                    "name": "Yoga Mat",
                    "description": "Elastic mat to practice yoga.",
                    "quantity": "1",
                    "unit_amount": {
                        "currency_code": "USD",
                        "value": "50.00"
                    },
                    "tax": {
                        "name": "Sales Tax",
                        "percent": "7.25"
                    },
                    "discount": {
                        "percent": "5"
                    },
                    "unit_of_measure": "QUANTITY"
                },
                {
                    "name": "Yoga t-shirt",
                    "quantity": "1",
                    "unit_amount": {
                        "currency_code": "USD",
                        "value": "10.00"
                    },
                    "tax": {
                        "name": "Sales Tax",
                        "percent": "7.25"
                    },
                    "discount": {
                        "amount": {
                            "currency_code": "USD",
                            "value": "5.00"
                        }
                    },
                    "unit_of_measure": "QUANTITY"
                }
            ],
            "configuration": {
                "partial_payment": {
                    "allow_partial_payment": True,
                    "minimum_amount_due": {
                        "currency_code": "USD",
                        "value": "20.00"
                    }
                },
                "allow_tip": True,
                "tax_calculated_after_discount": True,
                "tax_inclusive": False,
                "template_id": "TEMP-19V05281TU309413B"
            },
            "amount": {
                "breakdown": {
                    "custom": {
                        "label": "Packing Charges",
                        "amount": {
                            "currency_code": "USD",
                            "value": "10.00"
                        }
                    },
                    "shipping": {
                        "amount": {
                            "currency_code": "USD",
                            "value": "10.00"
                        },
                        "tax": {
                            "name": "Sales Tax",
                            "percent": "7.25"
                        }
                    },
                    "discount": {
                        "invoice_discount": {
                            "percent": "5"
                        }
                    }
                }
            }
        }
        data_json = json.dumps(data)
        print(data_json)
        print(type(data_json))
        response = requests.post('https://api-m.sandbox.paypal.com/v2/invoicing/invoices', headers=headers, data=data_json)
        return response


"""
        payment_term = {}
        payment_term['term_type'] = term_type
        payment_term['due_date'] = due_date

        detail = {}
        detail['invoice_number'] = invoice_number
        detail['reference'] = 'deal-ref'
        detail['currency_code'] = currency_code
        detail['note'] = note
        detail['invoice_date'] = date
        detail['term'] = term
        detail['memo'] = memo
        detail['payment_term'] = payment_term

        datajson = {}
        datajson['detail'] = detail
        datajson['invoicer'] = self.invoicer
        datajson['primary_recipients'] = self.recipients
        datajson['items'] = self.items

        data = datajson
        print(data)
        """

"""
client_id = 'ATgijFs8JZWdAPxMsNhN_Vl3VgZhIvzmPDwUCXjzMHdOFoOjM_mqXua1AaaKhiiEnyHlk8_tXoYsRZbc'
secret = 'ENu6GbuB-Fzc6Y0F7w1ouYhqQnkpyTUXEu3k7utvo3bqkjikJLk1GZKuolkR7Ymy2hNPpZUhXdW0Zf39'

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en_US',
}

data = {
    'grant_type': 'client_credentials'
}

response = requests.post('https://api-m.sandbox.paypal.com/v1/oauth2/token', headers=headers, data=data,
                         auth=(client_id, secret))

respjson = response.json()
access_token = respjson['access_token']
print(access_token)
"""
