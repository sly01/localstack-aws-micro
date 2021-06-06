resource "aws_dynamodb_table" "monitoring-table" {
  name           = "Monitoring"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "Country"

  attribute {
    name = "Country"
    type = "S"
  }

  tags = {
    Name        = "dynamodb-table-1"
    Environment = "production"
  }
}

resource "aws_dynamodb_table_item" "items" {
    count = length(var.countries)
  table_name = aws_dynamodb_table.monitoring-table.name
  hash_key   = aws_dynamodb_table.monitoring-table.hash_key

  item = <<ITEM
{
  "Country": {"S": "${var.countries[count.index]}"},
  "failedReplication": {"N": "0"},
  "failedRestore": {"N": "0"}
}
ITEM
}
