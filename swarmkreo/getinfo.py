import hid
for d in hid.enumerate():
    print(
        hex(d["vendor_id"]),
        hex(d["product_id"]),
        d.get("product_string"),
        d.get("usage_page"),
        d.get("interface_number"),
    )
