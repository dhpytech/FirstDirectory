let updateBtns;
let cart_items;
updateBtns = document.getElementsByClassName('update-cart');
cart_items = +document.getElementById('cart items').textContent;
for (let i=0;i < updateBtns.length; i++)
    {
        updateBtns[i].addEventListener('click', function ()
        {
            let itemId = this.dataset.item;
            let productId = this.dataset.product;
            let action = this.dataset.action;
            if (user === "AnonymousUser")
            {
                console.log('User does not login');
            }
            else
            {
                update_user_order(itemId, productId, action);
                cart_items += 1
                document.getElementById('cart items').innerHTML = cart_items
            }
        })
    }
function update_user_order(itemId, productId, action) {
    let url = '/home/update_item/'
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({"productId":productId, "action": action}),
        })
        .then(response =>{
        return response.json()}
        )
        .then(data =>{
            let quantityElement = document.getElementById(`${itemId}p_quantity`);
            let quantityValue = parseFloat(quantityElement.textContent);
            quantityValue = action === "remove" ? quantityValue - 1 : quantityValue + 1;
            quantityElement.innerHTML = quantityValue.toLocaleString("en-US");
            if (quantityValue === 0 && action === "remove") {
                quantityElement.parentElement.parentElement.remove();
                return
            }
            const checkBoxElement = document.getElementById(itemId);
            checkBoxElement.dataset.quantity = quantityValue.toString();
            const price = +checkBoxElement.dataset.price;
            const cost = price * quantityValue;
            document.getElementById(`${itemId}p_total`).innerHTML = cost.toLocaleString("en-US");
            let cost_total_element = document.getElementById(`cost_total`)
            let cost_total = parseFloat(cost_total_element.textContent.replace(/,/g, ''));
            cost_total = action === "remove" ? cost_total - price : cost_total + price;
            cost_total_element.innerHTML = cost_total.toLocaleString("en-US");
        })
}
