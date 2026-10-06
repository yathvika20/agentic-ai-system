import json
import os

examples = [
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."
            },
            {
                "role": "user",
                "content": "What is your return policy?"
            },
            {
                "role": "assistant",
                "content": "We offer a 30-day return policy for all products. Items must be unused and in their original packaging. Refunds are processed within 3-5 business days. Is there anything else I can help you with?"
            }
        ]
    },

    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."
            },
            {
                "role": "user",
                "content": "My order has not arrived after two weeks."
            },
            {
                "role": "assistant",
                "content": "I'm sorry to hear that. That is unusual for us. Please provide your order number so I can check its status and escalate the issue if needed."
            }
        ]
    },

    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."
            },
            {
                "role": "user",
                "content": "Where is my order 1001?"
            },
            {
                "role": "assistant",
                "content": "Order 1001 has been shipped and is expected to arrive within two business days."
            }
        ]
    },

    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."
            },
            {
                "role": "user",
                "content": "Can I cancel my order?"
            },
            {
                "role": "assistant",
                "content": "If your order has not been shipped yet, you can cancel it. Please share your order number so I can check its status."
            }
        ]
    },

    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."
            },
            {
                "role": "user",
                "content": "I want to speak with a human."
            },
            {
                "role": "assistant",
                "content": "Certainly. I'll escalate your request to a human support representative. They will contact you as soon as possible."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."
            },
            {
                "role": "user",
                "content": "How long does shipping take?"
            },
            {
                "role": "assistant",
                "content": "Standard shipping usually takes 3-5 business days, while express shipping takes 1-2 business days."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."
            },
            {
                "role": "user",
                "content": "Do you offer free shipping?"
            },
            {
                "role": "assistant",
                "content": "Yes. We offer free standard shipping on orders above $50."
            }
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"Do you offer free shipping?"},
            {"role":"assistant","content":"Yes. Orders above $50 qualify for free standard shipping."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"When will I receive my refund?"},
            {"role":"assistant","content":"Refunds are usually processed within 3-5 business days after the returned item is inspected."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"My product arrived damaged."},
            {"role":"assistant","content":"I'm sorry about that. Please upload photos of the damaged item, and we'll arrange a replacement or refund."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"Can I change my delivery address?"},
            {"role":"assistant","content":"Yes, if your order hasn't been shipped yet. Please provide your order number."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"What payment methods do you accept?"},
            {"role":"assistant","content":"We accept Visa, MasterCard, PayPal, UPI, and major debit and credit cards."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"Does this product include a warranty?"},
            {"role":"assistant","content":"Yes. Most products include a one-year manufacturer warranty."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"I placed my order by mistake."},
            {"role":"assistant","content":"If your order hasn't been shipped, we can cancel it. Please provide your order number."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"Is the wireless mouse in stock?"},
            {"role":"assistant","content":"Yes, the wireless mouse is currently in stock and ready for shipping."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"I forgot my password."},
            {"role":"assistant","content":"Click the 'Forgot Password' link on the login page and follow the instructions to reset your password."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"Do you have any discounts?"},
            {"role":"assistant","content":"We regularly offer seasonal promotions. Please check our website or subscribe to our newsletter for the latest offers."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"Can I download my invoice?"},
            {"role":"assistant","content":"Yes. You can download your invoice from the Orders section of your account after the purchase is completed."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"Why is my delivery delayed?"},
            {"role":"assistant","content":"Delivery delays can occur due to weather, carrier issues, or high demand. We'll provide updates as soon as they're available."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"I need to talk to a manager."},
            {"role":"assistant","content":"Certainly. I'll escalate your request to a supervisor, who will contact you as soon as possible."}
        ]
    },
    {
        "messages": [
            {"role":"system","content":"You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role":"user","content":"Thank you for your help."},
            {"role":"assistant","content":"You're welcome! If you have any more questions, feel free to contact us anytime."}
        ]
    },
    # Example 21
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I return a gift item?"},
            {"role": "assistant", "content": "Yes, gift items can be returned within 30 days if they are unused and in their original packaging."}
        ]
    },

    # Example 22
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "How do I track my order?"},
            {"role": "assistant", "content": "Once your order ships, you'll receive a tracking link by email."}
        ]
    },

    # Example 23
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "My package says delivered but I didn't receive it."},
            {"role": "assistant", "content": "I'm sorry to hear that. Please check with your neighbors and contact the carrier. If it's still missing, we'll investigate further."}
        ]
    },

    # Example 24
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I place an order over the phone?"},
            {"role": "assistant", "content": "Currently, orders can only be placed through our website or mobile app."}
        ]
    },

    # Example 25
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "How can I contact customer support?"},
            {"role": "assistant", "content": "You can contact us via chat, email, or phone during business hours."}
        ]
    },

    # Example 26
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I modify my order after placing it?"},
            {"role": "assistant", "content": "If the order has not entered processing, we can help modify it. Please provide your order number."}
        ]
    },

    # Example 27
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Do you restock out-of-stock products?"},
            {"role": "assistant", "content": "Yes, many products are restocked regularly. You can sign up for stock notifications."}
        ]
    },

    # Example 28
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "How do I apply a coupon code?"},
            {"role": "assistant", "content": "Enter your coupon code during checkout before completing your payment."}
        ]
    },

    # Example 29
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I use multiple coupons?"},
            {"role": "assistant", "content": "Only one promotional coupon can be applied per order unless otherwise specified."}
        ]
    },

    # Example 30
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Is my payment information secure?"},
            {"role": "assistant", "content": "Yes. We use secure encryption and trusted payment gateways to protect your information."}
        ]
    },

    # Example 31
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I preorder upcoming products?"},
            {"role": "assistant", "content": "Yes, eligible products will display a preorder option before their release date."}
        ]
    },

    # Example 32
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "My payment failed. What should I do?"},
            {"role": "assistant", "content": "Please verify your payment details or try another payment method. Contact your bank if the issue continues."}
        ]
    },

    # Example 33
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I save items for later?"},
            {"role": "assistant", "content": "Yes. You can add products to your wishlist for future purchases."}
        ]
    },

    # Example 34
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "What if I entered the wrong email address?"},
            {"role": "assistant", "content": "Please contact customer support with your order details so we can update your email if possible."}
        ]
    },

    # Example 35
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I return only one item from my order?"},
            {"role": "assistant", "content": "Yes. Individual items can be returned if they meet our return policy requirements."}
        ]
    },

    # Example 36
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Do you offer same-day delivery?"},
            {"role": "assistant", "content": "Same-day delivery is available only in selected locations."}
        ]
    },

    # Example 37
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I schedule my delivery?"},
            {"role": "assistant", "content": "Delivery scheduling is available for selected products and regions."}
        ]
    },

    # Example 38
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Do you have a mobile app?"},
            {"role": "assistant", "content": "Yes. Our mobile app is available for both Android and iOS devices."}
        ]
    },

    # Example 39
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "How do I delete my account?"},
            {"role": "assistant", "content": "Please contact customer support to request permanent account deletion."}
        ]
    },

    # Example 40
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Do you sell gift cards?"},
            {"role": "assistant", "content": "Yes, digital gift cards are available in multiple denominations."}
        ]
    },

    # Example 41
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I use a gift card with a coupon?"},
            {"role": "assistant", "content": "Yes, gift cards can usually be combined with one valid promotional coupon."}
        ]
    },

    # Example 42
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "What are your business hours?"},
            {"role": "assistant", "content": "Customer support is available Monday through Friday from 9 AM to 6 PM."}
        ]
    },

    # Example 43
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I reorder a previous purchase?"},
            {"role": "assistant", "content": "Yes. You can reorder items from your order history if they are currently in stock."}
        ]
    },

    # Example 44
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "How do I update my shipping address?"},
            {"role": "assistant", "content": "Go to your account settings to update your default shipping address for future orders."}
        ]
    },

    # Example 45
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I return an item without the original box?"},
            {"role": "assistant", "content": "Original packaging is preferred, but please contact us to discuss your specific situation."}
        ]
    },

    # Example 46
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "How do I unsubscribe from promotional emails?"},
            {"role": "assistant", "content": "Click the unsubscribe link at the bottom of any promotional email or update your notification settings."}
        ]
    },

    # Example 47
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Do you have live chat support?"},
            {"role": "assistant", "content": "Yes, our live chat is available during customer support business hours."}
        ]
    },

    # Example 48
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "My order arrived incomplete."},
            {"role": "assistant", "content": "I'm sorry about that. Please tell us which items are missing, and we'll resolve the issue promptly."}
        ]
    },

    # Example 49
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Can I request express delivery after placing my order?"},
            {"role": "assistant", "content": "If your order has not shipped yet, we'll check whether express shipping can be added."}
        ]
    },

    # Example 50
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for AcmeCorp. Be empathetic and concise."},
            {"role": "user", "content": "Thank you for your assistance."},
            {"role": "assistant", "content": "You're very welcome! We're happy to help. If you have any more questions, please don't hesitate to contact us."}
        ]
    }
]

os.makedirs("data/training", exist_ok=True)

with open("data/training/train.jsonl", "w", encoding="utf-8") as f:
    for ex in examples:
        f.write(json.dumps(ex) + "\n")

print(f"Dataset created successfully with {len(examples)} examples.")