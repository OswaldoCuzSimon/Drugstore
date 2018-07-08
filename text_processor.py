from sympy import Polygon


class TextProcessor(object):

    def getPolygon(self, vertices):
        p1, p2, p3, p4 = tuple((i['x'], i['y']) for i in vertices)
        return Polygon(p1, p2, p3, p4)

    def get_polygons(self, vertices, textAnnotations):
        polygons = [self.getPolygon(v) for v in vertices]
        for i, phrase in enumerate(textAnnotations):
            polygons[i].label = phrase['description']
        return polygons

    def get_phrases(self, vertices, textAnnotations):
        polygons = self.get_polygons(vertices, textAnnotations)
        all_text = polygons[0].label.strip().split('\n')
        copy = polygons[:]
        poly_phrase = []
        for phrase in all_text:
            copy, _ = self.find_polygon(copy, phrase)
            if _:
                poly_phrase.append(_)
        area_phrase = self.calc_area_by_phrase(poly_phrase)
        weight_phrase = [((ap[0] / len(ap[1])).evalf(), ap[1])
                         for ap in area_phrase]
        weight_phrase = sorted(
            weight_phrase, reverse=True, key=lambda wp: wp[0])
        return [i[1] for i in weight_phrase]

    @staticmethod
    def find_polygon(polygons, phrase):
        poly_phrase = []
        polygon_indeces = []
        for word in phrase.split(" "):
            for i, p in enumerate(polygons):
                if p.label == word:
                    poly_phrase.append(p)
                    polygon_indeces.append(i)
                    break
        for i in sorted(polygon_indeces, reverse=True):
            del polygons[i]

        return polygons, poly_phrase

    @staticmethod
    def calc_area_by_phrase(poly_phrase):
        area_phrase = []
        for pp in poly_phrase:
            area = sum([p.area for p in pp])
            phrase = " ".join([p.label for p in pp])
            area_phrase.append((area, phrase))
        return area_phrase
