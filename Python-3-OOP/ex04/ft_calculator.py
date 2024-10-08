class calculator:
    """
    A calculator class that is able to do calculations
    (dot product, addition, subtraction) of 2 vectors.
    Methods:
        dotproduct(V1, V2): calculates the dot product of two vectors.
        add_vec(V1, V2): adds two vectors.
        sous_vec(V1, V2): subtracts two vectors.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates the dot product of two vectors.
        """
        dot_product = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dot product is: {dot_product}")
        return None

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        adds two vectors.
        """
        add_vector = [float(v1 + v2) for v1, v2 in zip(V1, V2)]
        print(f"Add vector is: {add_vector}")
        return None

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        subtracts two vectors.
        """
        sous_vector = [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        print(f"Sous vector is: {sous_vector}")
        return None
