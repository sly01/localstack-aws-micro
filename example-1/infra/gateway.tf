# api gateway with lambda proxy
resource "aws_api_gateway_rest_api" "MyDemoAPI" {
  name        = "MyDemoAPI"
  description = "This is my API for demonstration purposes"
}

resource "aws_api_gateway_resource" "MyDemoResource" {
  rest_api_id = aws_api_gateway_rest_api.MyDemoAPI.id
  parent_id   = aws_api_gateway_rest_api.MyDemoAPI.root_resource_id
  path_part   = "myresource"
}

resource "aws_api_gateway_method" "MyDemoMethod" {
  rest_api_id   = aws_api_gateway_rest_api.MyDemoAPI.id
  resource_id   = aws_api_gateway_resource.MyDemoResource.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "MyDemoIntegration" {
  rest_api_id = aws_api_gateway_rest_api.MyDemoAPI.id
  resource_id = aws_api_gateway_method.MyDemoMethod.resource_id
  http_method = aws_api_gateway_method.MyDemoMethod.http_method

  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.test_lambda.invoke_arn
}

resource "aws_api_gateway_deployment" "example" {
  rest_api_id = aws_api_gateway_rest_api.MyDemoAPI.id
  stage_name  = "test"
  depends_on = [
    aws_api_gateway_integration.MyDemoIntegration
  ]
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_lambda_permission" "allow_gateway" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.test_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.MyDemoAPI.execution_arn}/*/*"
}

output "api_id" {
  value = aws_api_gateway_deployment.example.rest_api_id
}

output "endpoint" {
  value = "http://localhost:4566/restapis/${aws_api_gateway_deployment.example.rest_api_id}/test/_user_request_/"
}
