from werkzeug.utils import secure_filename

class File():
    def uploadFile(self, file):
        filename = secure_filename(file.filename)

        with open('static/uploads/' + filename, "wb") as fp:
            for item in file:
                fp.write(item)

        return filename