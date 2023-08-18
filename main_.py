from email_builder import EmailBuilder


def main():
    email = EmailBuilder() \
        .add_from("info@campbelltech.io") \
        .add_to("john@gmail.com") \
        .add_to("jane@yahoo.com") \
        .add_cc("jones@campbelltech.io") \
        .with_subject("The Builder Pattern Tutorial") \
        .with_body("Checkout this awesome blog on how to code the Builder Pattern") \
        .add_attachment("Builder-Pattern.pdf") \
        .build()
    email.send()


if __name__ == '__main__':
    main()
