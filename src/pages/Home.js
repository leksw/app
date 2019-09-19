import React, { useState } from 'react';

import ItemsLIst from './Items/ItemsList';
import Button from '../components/Button';

export default function Home() {
  const [items, setItems] = useState([
    { id: 1, title: 'First item', description: 'First description' },
    { id: 2, title: 'Second item', description: 'Second description' },
    { id: 3, title: 'Third item', description: 'Third description' },
  ]);

  const addItem = () => () => {
    setItems([
      ...items,
      ...[
        {
          id: 4,
          title: 'Fore item',
          description: 'Third description',
        },
      ],
    ]);
    // setItems(items);
  };

  return (
    <div className="wrapper">
      <h1>Trade</h1>
      <h4>{items.length}</h4>
      <ItemsLIst items={items} />
      <Button onClick={addItem()}>Add item</Button>
    </div>
  );
}
