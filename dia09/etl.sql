SELECT IdCliente,
        sum(QtdePontos) AS TotalPontos,
        count(DISTINCT IdTransacao) as QtTransacoes 

FROM transacoes

GROUP BY idCliente




