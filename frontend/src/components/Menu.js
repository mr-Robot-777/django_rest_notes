import React from 'react'
import {Link} from "react-router-dom";

const Menu = () => {
    return (
        <div className='menu'>
            <Link to='/projects'>Projects</Link>
            <Link to='/todos'>Todos</Link>
            <Link to='/users'>Users</Link>

            {/*<a href="#">Users  </a>*/}
            {/*<a href="#">Info  </a>*/}
            {/*<a href="#">Login  </a>*/}
        </div>
    )
}

export default Menu
