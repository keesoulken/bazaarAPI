from mlwbzr import Client
from mlwbzr.exceptions import BazaarException

test_hash = ""

client = Client(api_key="API_KEY_HERE")
try:
    response = client.send_file("eicar.txt", anonymous=1, tags=['txt', 'eicar'])
    print("Insert status: ", response['status'])

    filecontent = client.get_file(test_hash)
    print("Filecontent: ", filecontent[:10])

    sample = client.get_info(test_hash)
    print("Sample name: ", sample.file_name)
    print("Sample md5: ", sample.md5_hash)

    r = client.update(test_hash, 'links', 'test123')
    print("Update link status: ", r['status'])

    r = client.add_comment(test_hash, 'tested comment')
    print("Add comment status: ", r['status'])
except BazaarException:
    pass

samples = client.get_recent('time')
print("Recent samples count:", len(samples))
print("Recent samples names:")
print(', '.join(x.file_name for x in samples))

samples = client.get_subjectinfo("Ekitai Data Inc.")
print("By subject CN: ")
for sample in samples:
    print(sample.file_name, sample.sha256_hash)

print("CSCB: ")
certs = client.get_cscb()
for cert in certs:
    print(cert.serial_number, cert.cscb_reason, cert.cscb_listed)

