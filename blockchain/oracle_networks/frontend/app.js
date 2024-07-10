import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

const App = () => {
    const [nodes, setNodes] = useState([]);
    const [nodeBalance, setNodeBalance] = useState(0);
    const [transaction, setTransaction] = useState({ from: '', to: '', amount: 0 });

    useEffect(() => {
        const web3 = new Web3(new Web3.providers.HttpProvider('https://example.com/blockchain'));
        const oracleNetworkContract = new web3.eth.Contract(oracleNetworkABI, '0x...ContractAddress...');

        oracleNetworkContract.methods.getNodes().call().then(nodes => setNodes(nodes));
        oracleNetworkContract.methods.getNodeBalance('0x...NodeAddress...').call().then(balance => setNodeBalance(balance));
    }, []);

    const handleTransaction = async () => {
        const web3 = new Web3(new Web3.providers.HttpProvider('https://example.com/blockchain'));
        const oracleNetworkContract = new web3.eth.Contract(oracleNetworkABI, '0x...ContractAddress...');

        await oracleNetworkContract.methods.sendTransaction(transaction.from, transaction.to, transaction.amount).send({ from: '0x...UserAddress...' });
    };

    return (
        <div>
            <h1>Oracle Network Interface</h1>
            <ul>
                {nodes.map(node => <li key={node}>{node}</li>)}
            </ul>
            <p>Node Balance: {nodeBalance}</p>
            <form onSubmit={handleTransaction}>
                <input type="text" value={transaction.from} onChange={e => setTransaction({ ...transaction, from: e.target.value })} />
                <input type="text" value={transaction.to} onChange={e => setTransaction({ ...transaction, to: e.target.value })} />
                <input type="number" value={transaction.amount} onChange={e => setTransaction({ ...transaction, amount: e.target.value })} />
                <button type="submit">Send Transaction</button>
            </form>
        </div>
    );
};

export default App;
