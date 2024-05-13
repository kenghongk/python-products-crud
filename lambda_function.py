import json
from products import products  

def lambda_handler(event, context):
    action = event.get('action')
    product_id = event.get('product_id')
    product_name = event.get('product_name')
    product_description = event.get('product_description')
    product_price = event.get('product_price')
    product_quantity = event.get('product_quantity')
    product_status = event.get('product_status')

    if action == 'create':
        try:
            products.create_product(product_id, product_name, product_description, product_price, product_quantity, product_status)
            return {
                'statusCode': 200,
                'body': json.dumps('Product created successfully')
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error creating product: {str(e)}')
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid action')
        }
