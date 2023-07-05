def solution(gems):
    gem_dict = {}
    length = len(gems)
    min_distance = 2e9
    min_gem = 2e9
    max_gem = -2e9

    def update_distance(s, e):
        nonlocal min_distance, min_gem, max_gem
        if 0 <= e - s < min_distance:
            min_distance = e - s
            min_gem = s + 1
            max_gem = e

    end = 0
    gem_type = len(set(gems))

    for start in range(length):

        while end < length:
            if len(gem_dict) == gem_type:
                break
            if gems[end] not in gem_dict:
                gem_dict[gems[end]] = 0
            gem_dict[gems[end]] += 1
            end += 1

        if len(gem_dict) == gem_type:
            update_distance(start, end)

        gem_dict[gems[start]] -= 1

        if not gem_dict[gems[start]]:
            del gem_dict[gems[start]]

    return [min_gem, max_gem]
