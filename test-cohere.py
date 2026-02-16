import cohere

co = cohere.ClientV2(api_key="<YOUR API KEY>")

res = co.chat(
    model="model-name-of-your-choice",
    messages=[
        {
            "role": "user",
            "content": "Write a title for a blog post about API design. Only output the title text.",
        }
    ],
)

print(res.message.content[0].text)
# "The Ultimate Guide to API Design: Best Practices for Building Robust and Scalable APIs"
