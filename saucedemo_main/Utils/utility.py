import csv
import json


class Utility:

  def read_csv(file_name):
    with open(file_name) as csvfile:
      reader = csv.reader(csvfile)
      # This skips the first row of the CSV file.
      next(reader)
      data = list(reader)
      csvfile.close()
    return data

  def read_txt(file_name, delimeter=','):
    txtfile = open(file_name, 'r')
    content_list = txtfile.read()
    txtfile.close()

    return content_list.split(delimeter)

  def read_json(file_name):
    with open(file_name, 'r') as jsonfile:
      reader = json.load(jsonfile)
      jsonfile.close()
    return reader
