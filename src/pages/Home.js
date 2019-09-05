import React from 'react';

import ItemsLIst from './Items/ItemsList';

export default function Home() {
  const items = [
    { id: 1, title: 'First item', description: 'First description' },
    { id: 2, title: 'Second item', description: 'Second description' },
    { id: 3, title: 'Third item', description: 'Third description' },
  ];

  return (
    <div className="wrapper">
      <h1>Trade</h1>
      <ItemsLIst items={items} />
    </div>
  );
}
