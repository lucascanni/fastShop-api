from fastapi import APIRouter, Depends, HTTPException, status, Request, Header, Depends, Body
from fastapi.responses import RedirectResponse
import stripe


router = APIRouter(
    prefix='/stripe',
    tags=['Stripe']
)

stripe.api_key = config['STRIPE_SK']
YOUR_DOMAIN = 'http://localhost'

@router.post('/checkout')
async def stripe_checkout():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price': 'price_1O51yMGQ2alTbrjjBxhKeDz5',
                'quantity': 1,
            }],
            mode='subscription',
            payment_method_types=['card'],
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return checkout_session
        response = RedirectResponse(url=checkout_session['url'])
    except Exception as e:
        return e

@router.post('/webhook')
async def webhook_received(request: Request, stripe_signature: str = Header(None)):
    webhook_secret = 'whsec_c6d527fde2ddb0f3a106d2a628eab77e999cb8e885ca7056657ed726d005b2d0'
    data = await request.body()
    try:
        event = stripe.Webhook.construct_event(
            payload=data, 
            sig_header=stripe_signature, 
            secret=webhook_secret
        )
        event_data = event['data']
    except Exception as e:
        return {"error": str(e)}
    
    event_type = event['type']
    if event_type == 'checkout.session.completed':
        print('Checkout session completed')
    elif event_type == 'invoice.paid':
        print('Invoice paid')
    elif event_type == 'invoice.payment_failed':
        print('Invoice payment failed')
    else:
        print(f'Unhandled event: {event_type}')

    return {"status": "success"}



@router.post('/success')
async def success():
    return "test"