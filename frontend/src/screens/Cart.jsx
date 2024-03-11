import { useDispatch, useSelector } from 'react-redux';
import { removeFromCart, updateCartQuantity } from '../redux/cart.slice';
import Checkout from '../components/Checkout';

export default function CartScreen() {
  const cartReducerState = useSelector((state) => state.cartReducer);
  const dispatch = useDispatch();
  const { cartItems } = cartReducerState;

  const subtotal = cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);

  return (
    <div className="relative overflow-x-auto">
      <div className="flex justify-center">
        <div className="w-full md:w-2/3 card text-center shadow p-3 mb-5 bg-white rounded">
          <div className="text-center m-5">My Cart</div>
          <div className="overflow-x-auto">
            <table className="table-auto w-full">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Price</th>
                  <th>Quantity</th>
                  <th>Total Price</th>
                  <th>Delete</th>
                </tr>
              </thead>
              <tbody>
                {cartItems.map((item) => (
                  <tr key={item.id}>
                    <td>{item.name}</td>
                    <td>{item.price}</td>
                    <td>
                      <input
                        type="number"
                        value={item.quantity}
                        onChange={(e) =>
                          dispatch(
                            updateCartQuantity({
                              id: item.id,
                              quantity: parseInt(e.target.value),
                            })
                          )
                        }
                      />
                    </td>
                    <td>{(item.quantity * item.price).toFixed(2)}</td>
                    <td>
                      <i
                        className="far fa-trash-alt delete-icon"
                        onClick={() => dispatch(removeFromCart(item))}
                      ></i>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <hr />
          <h2 className="text-center">SubTotal: {subtotal.toFixed(2)} Rp/-</h2>
          <hr />
          <Checkout amount={subtotal} />
        </div>
      </div>
    </div>
  );
}
