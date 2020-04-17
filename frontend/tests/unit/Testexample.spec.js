import Vue from "vue";
import TestExample from "@/components/TestExample";
import RecipeDetail from "@/view/RecipeDetail";

let Constructor;
let vm;
let frist;
let second;

// 초기화
beforeEach(() => {
  Constructor = Vue.extend(TestExample);
  vm = new Constructor().$mount();

  frist = vm._data.frist;
  second = vm._data.second;
});

describe("TestExample.vue", () => {
  describe("유효성 검사", () => {
    it("숫자가 아닌 Null 또는 문자열을 입력할 경우 결과값이 에러(NaN)인지 확인한다.", () => {
      second = "가";
      // NaN값인 경우
      expect(vm.plus(frist, second)).toBeNaN();
      expect(vm.minus(frist, second)).toBeNaN();
      expect(vm.multiply(frist, second)).toBeNaN();
      expect(vm.divide(frist, second)).toBeNaN();
    });
    it("0으로 곱하기 또는 나누기 하려고 하는지 확인한다.", () => {
      second = 0;
      // toBeFalsy : if 문의 리턴값이 false 인 경우
      expect(vm.multiply(frist, 0)).toBeFalsy();
      expect(vm.divide(frist, 0)).toBeFalsy();
    });
  });
  describe("사칙연산 테스트", () => {
    it("더하기의 결과값을 비교하여 일치한지 확인한다.", () => {
      // toBe : 기본값을 비교할때 사용
      expect(vm.plus(frist, second)).toBe(9);
    });
    it("뺴기 결과값을 비교하여 정수인지 음수인지 확인한다.", () => {
      expect(vm.minus(frist, second)).toBe(5);
    });
    it("곱하기의 결과값을 비교하여 일치한지 확인한다.", () => {
      expect(vm.multiply(frist, second)).toBe(14);
    });
    it("나누기의 결과값을 비교하여 소스점 반올림이 되었는지 확인한다.", () => {
      // toBeCloseTo : 소수점 다음에 확인할 자리 수를 제어하는데 사용
      expect(vm.divide(frist, second)).toBeCloseTo(4, 5);
    });
  });
});

jest.mock("axios", () => ({
  get: jest.fn()
}));

import axios from "axios";

describe("RecipeMeterial.vue", () => {
  describe("API 테스트", () => {
    it("Calls axios.get", () => {
      expect(axios.get).toBeCalledWith("http://localhost:8080/hello");
    });
  });
});
