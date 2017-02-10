import dropbox


dbx = dropbox.Dropbox("I4gEG90KcJAAAAAAAAACNBpxYbWSAgK4hpufdGTK2ox1eIlhU9Nfzg6BeZS9ttz9")

for entry in dbx.files_list_folder('').entries:
	print(entry.name)

dbx.files_download('/iiti.csv')
