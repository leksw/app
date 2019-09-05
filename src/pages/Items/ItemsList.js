import React from 'react';
import PropTypes from 'prop-types';

import Item from './Item';

const styles = {
  ul: {
    listStyle: 'none',
    margin: 0,
    padding: 0,
  },
};

export default function ItemsList(props) {
  return (
    <ul style={styles.ul}>
      {props.items.map((item, idx) => {
        return <Item item={item} key={item.id} index={idx} />;
      })}
    </ul>
  );
}

ItemsList.propTypes = {
  items: PropTypes.arrayOf(PropTypes.object).isRequired,
};
