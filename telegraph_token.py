from telegraph import Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name=input("Enter a username for your Telegra.ph : Bumble_beeeeee"))

print(f"Your Telegra.ph token ==>  {telegraph.get_access_token()}")
