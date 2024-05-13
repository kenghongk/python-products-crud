import boto3
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('products')

# Function to generate product slug based on product name
def generate_slug(product_name):
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', product_name).lower()
    return slug

def create_product(product_id, product_name, product_description, product_price, product_quantity, product_status):
    product_slug = generate_slug(product_name)
    table.put_item(
        Item={
            'product_id': product_id,
            'product_name': product_name,
            'product_slug': product_slug,
            'product_description': product_description,
            'product_price': product_price,
            'product_quantity': product_quantity,
            'product_status': product_status
        }
    )

def read_product(product_id):
    response = table.get_item(
        Key={
            'product_id': product_id,
        }
    )
    return response.get('Item', None)

def update_product(product_id, update_expression, expression_attribute_values):
    table.update_item(
        Key={
             'product_id': product_id,
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values
    )

def delete_product(product_id):
    table.delete_item(
        Key={
           'product_id': product_id,
        }
    )
