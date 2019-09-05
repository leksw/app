import React from 'react';
import PropTypes from 'prop-types';

function Item({ item, index }) {
  return (
    <li>
      <strong>{index + 1}</strong>&nbsp;
      {item.title}
    </li>
  );
}

Item.propTypes = {
  item: PropTypes.object.isRequired,
  index: PropTypes.number,
};

export default Item;
